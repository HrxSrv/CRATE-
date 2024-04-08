
import './App.css';
import {BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './components/Header/Header';
import Footer from "./components/Footer/Footer";
import Home from "./components/Home/Home";
import Category from "./components/Category/Category";
import SingleProduct from "./components/SingleProduct/SingleProduct";
import Product from "./components/Products/Products"
import AppContext from "./utils/context";
import LoginPage from './components/authPage/LoginPage';
function App() {
  return (
    <div className="App">
       <BrowserRouter>
       <AppContext>
       <Header/>
          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/category/:id" element={<Category/>}/>
            <Route path="/product/:id" element={<Product/>}/>
            <Route path="/SingleProduct/:id" element={<SingleProduct/>}/>
            <Route path="/LoginPage/:id" element={<LoginPage/>}/>
          </Routes>
       <Footer/>   
       </AppContext>
       </BrowserRouter>
    </div>
  );
}

export default App;
