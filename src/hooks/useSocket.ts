import { useEffect, useState } from "react";
import { io, Socket } from "socket.io-client";

interface ISocketError {
  message: string;
  type: string;
}

const useSocket = () => {
  const [connected, setConnected] = useState<boolean>(false);
  const [connecting, setConnecting] = useState<boolean>(true);
  const [disconnected, setDisconnected] = useState<boolean>(false);
  const [socketIO, setSocketIO] = useState<Socket | null>(null);
  const [error, setError] = useState<ISocketError | null>(null);
  const wsUrl: string | undefined = process.env.REACT_APP_WS_ENDPOINT;

  useEffect(() => {
    const initSocket: Socket | null = io(`${wsUrl}`, {
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionDelayMax: 5000,
      reconnectionAttempts: 99999,
      autoConnect: true,
    });
    setSocketIO(initSocket);
    return () => {
      socketIO && socketIO.disconnect();
    };
  }, []);

  if (socketIO) {
    // socket.io is connected
    socketIO.on("connect", () => {
      setConnected(true);
      setDisconnected(false);
      setConnecting(false);
      setError(null);
    });

    socketIO.on("connect_error", (err) => {
      setError({ message: err.message, type: "connect_error" });
    });

    socketIO.on("open", () => {
      // connection open
    });

    socketIO.on("close", () => {
      // connection closed listener
    });

    socketIO.on("disconnect", (reason) => {
      setConnected(false);
      setDisconnected(true);
      if (reason === "io server disconnect") {
        // the disconnection was initiated by the server, you need to reconnect manually
        socketIO.connect();
      }
      setError({ message: reason, type: "disconnect" });
    });

    socketIO.on("reconnect", (attemptNumber) => {
      console.log(">App ws-> reconnect", attemptNumber);
      setConnecting(false);
    });

    socketIO.on("reconnect_attempt", (attemptNumber) => {
      console.log(">App ws-> reconnect_attempt", attemptNumber);
      setConnecting(true);
    });
  }

  return { socket: socketIO, connected, disconnected, connecting, error };
};

export default useSocket;
