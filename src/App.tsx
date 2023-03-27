import { useState } from "react";
import "./App.css";
import useSocket from "./hooks/useSocket";

function App() {
  const [countries, setCountries] = useState<string[]>([]);
  const { socket, connected, disconnected, connecting } = useSocket();

  // Listen for the visit_random_country_generator message to emit from the server
  socket?.on("visit_random_country_generator", (res) => {
    const { data } = res;
    setCountries([...countries, data]);
    socket.emit("received_random_country", data);
  });

  // Test socket disconnect/reconnect
  const toggleConnection = () => {
    if (socket) {
      connected ? socket?.close() : socket.connect();
    }
  };
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <div>Connecting: {`${connecting}`}</div>
          <div>Connected: {`${connected}`}</div>
          <div>Disconnected: {`${disconnected}`}</div>
        </div>
        <div>
          <button onClick={toggleConnection}>
            {connected ? `Disconnect` : `Connect`}
          </button>
        </div>
        <div>
          {countries.map((country: string, countryIndex: number) => (
            <div key={`country-${countryIndex}`}>{country}</div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
