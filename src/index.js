import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

const Index = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/data'); // Adjust the URL as per your Flask server
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>React Client for Flask Server</h1>
      {data ? <App data={data} /> : <p>Loading...</p>}
    </div>
  );
};

ReactDOM.render(<Index />, document.getElementById('root'));