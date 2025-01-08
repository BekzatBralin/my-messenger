import asyncio
import websockets

clients = set()

async def handle_connection(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            # Рассылаем сообщение всем клиентам
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        print("Клиент отключился")
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Сервер запущен на ws://localhost:8765")
        await asyncio.Future()  # Блокируем выполнение для работы сервера

if __name__ == "__main__":
    asyncio.run(main())
