import { useState } from "react";
import dayjs from "dayjs";
import "./App.css";
import useSocket from "./hooks/useSocket";
interface IPingPongMessage {
  type: "ping" | "pong";
  message: string;
  timestamp: string;
}

function App() {
  const [cars, setCars] = useState<string[]>([]);
  const [pingPongSever, setPingPongServer] = useState<IPingPongMessage[]>([]);
  const { socket, connected, disconnected, connecting } = useSocket();

  // Listen for the visit_random_country_generator message to emit from the server
  socket?.on("visit_random_country_generator", (res) => {
    const { data } = res;
    setCars([...cars, data]);
    socket.emit("received_random_country", data);
  });

  // Receive Pong message from server
  socket?.on("pong_server", (res) => {
    setPingPongServer([...pingPongSever, res]);
  });

  // Test socket disconnect/reconnect
  const toggleConnection = () => {
    if (socket) {
      connected ? socket?.close() : socket.connect();
    }
  };

  const pingServer = () => {
    socket?.emit("ping_server");
    const now = dayjs().format("YYYY-MM-DD hh:mm:ss");
    setPingPongServer([
      ...pingPongSever,
      {
        type: "ping",
        message: "Ping",
        timestamp: now,
      },
    ]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="websocket-wrapper">
          <b>Socket status</b>
          <pre className="code-format">
            <div>Connecting: {`${connecting}`}</div>
            <div>Connected: {`${connected}`}</div>
            <div>Disconnected: {`${disconnected}`}</div>
          </pre>
          <div>
            <button onClick={toggleConnection}>
              {connected ? `Disconnect` : `Connect`}
            </button>
          </div>
        </div>
        <div className="websocket-wrapper">
          <div>
            <b>Ping Pong messages</b>
            <pre className="code-format">
              {pingPongSever.map(
                (pingPongData: IPingPongMessage, pingPongIndex: number) => (
                  <div key={`ping-pong-${pingPongIndex}`}>
                    <span className={pingPongData?.type}>
                      {pingPongData?.type === "pong" ? "Server" : "Client"}
                    </span>
                    {` message: ${pingPongData?.message} @ ${pingPongData?.timestamp}`}
                  </div>
                )
              )}
            </pre>
            <button onClick={pingServer}>Ping Server</button>
          </div>
        </div>
        <div>
          {cars.map((car, carIndex) => (
            <div key={`car-${carIndex}`}>{car}</div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
