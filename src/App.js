import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [inputValue, setInputValue] = useState('');

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/data'); // Adjust the endpoint as necessary
      setData(response.data);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/data', { value: inputValue }); // Adjust the endpoint as necessary
      setData(response.data);
      setInputValue('');
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h1>React Client for Flask Server</h1>
      {error && <p>Error: {error}</p>}
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={inputValue} 
          onChange={(e) => setInputValue(e.target.value)} 
          placeholder="Enter value" 
          required 
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;