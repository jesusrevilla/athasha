#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets
import random

logging.basicConfig()

STATE = {"value": 0}

USERS = set()

SCHEMA = {"type":"schema","points":[
    {"name":"Start Button Line 01", "type":"boolean", "value":"off"},
    {"name":"Speed Line 13", "type":"analog", "value":8},
    {"name":"Buzzer Line 07", "type":"boolean", "value":"off"},
    {"name":"Green Light Line 90", "type":"boolean", "value":"on"},
    {"name":"Temperature Oven Line 04", "type":"analog", "value":3},
    {"name":"Emergency Stop Line 08", "type":"boolean", "value":"on"},
    {"name":"Start button line 24", "type":"boolean", "value":"on"},
    ]}

def increase(id):
    id = int(id)
    SCHEMA["points"][id]["value"] += 1

def decrease(id):
    id = int(id)
    SCHEMA["points"][id]["value"] -= 1

def toggle(id):
    id = int(id)
    if SCHEMA["points"][id]["value"] == "on":
        SCHEMA["points"][id]["value"] = "off"
    else:
        SCHEMA["points"][id]["value"] = "on"

def initial_state():
    point_state_lst = []
    for point in SCHEMA['points']:
        point_state_lst.append(point["value"])
    return json.dumps({"type":"initial_values","values":point_state_lst})

def change_event(id):
    # random select one point
    return json.dumps({"type":"change", "id":id, "value":SCHEMA["points"][int(id)]["value"]})
    #return json.dumps(SCHEMA)

def state_event():
    return json.dumps({"type": "state", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def schema_event():
    return json.dumps(SCHEMA)

async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_schema():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = schema_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_change(id):
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = change_event(id)
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def screen(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    await websocket.send(schema_event())
    await websocket.send(initial_state())

    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "decrease":
                decrease(data["id"])
                await notify_change(data["id"])
            elif data["action"] == "increase":
                increase(data["id"])
                await notify_change(data["id"])
            elif data["action"] == "toggle":
                toggle(data["id"])
                await notify_change(data["id"])
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)

start_server = websockets.serve(screen, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()