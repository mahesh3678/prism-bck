"""Request-scoped Socket.IO rooms for the live RAG visualizer."""


def register_trace_events(sio):
    @sio.on("join_trace")
    async def join_trace(sid, data):
        trace_id = (data or {}).get("traceId")
        if not trace_id:
            return {"ok": False}
        await sio.enter_room(sid, f"trace_{trace_id}")
        return {"ok": True}

    @sio.on("leave_trace")
    async def leave_trace(sid, data):
        trace_id = (data or {}).get("traceId")
        if trace_id:
            await sio.leave_room(sid, f"trace_{trace_id}")
