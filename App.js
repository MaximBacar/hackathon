import './App.css';
import React from 'react';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './components/MainPage';
import Footer from './components/Footer';

function App() {
  return (
    <>
    <Router>
      <MainPage/>
      <Navbar/>
      <Footer/>
      <Routes>
        <Route path='/' />
      </Routes>
    </Router>
    </>
  );
}

export default App;
