import "./Header.scss";
import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import Cart from "../Cart/Cart"
import {AiOutlineHeart} from 'react-icons/ai' 
import {AiOutlineLogin} from 'react-icons/ai' 
import {AiOutlineShoppingCart} from 'react-icons/ai' 
import { useState} from "react";
import LoginPage from "../authPage/LoginPage";
import Search from "./Search/Search";
function Header() {
  const [slideCart, setSlidecart] = useState(false);
  const [authTile,setAuthtile] = useState(false);
  const [scrolled,setScrolled]=useState(false);
  const onScroll= ()=>{
    const offset=window.scrollY;
    if(offset>80){
      setScrolled(true);
    }
    else{
      setScrolled(false);
    }
  }
  window.addEventListener("scroll",onScroll);
  return (
    <div className="header">  
    <div className={scrolled?"Nav Navsticky":"Nav"}>
      <img alt="" src={require('../../assets/CRATE-logos_transparent.png')}/>
    <Search className/>
   <div className='nav2'>
   <div className='login'  onClick={()=>setAuthtile(x=>!x)}>
    <AiOutlineLogin className='loginIcon' size={"25px"} />
    <p>Login</p>
    </div>
   <div className='cart' onClick={()=>setSlidecart(x=>!x)}>
    <AiOutlineShoppingCart size={"25px"} />
   <span><p>9</p></span>
    <p>Cart</p>
   </div>
   <div className='wish'>
   <AiOutlineHeart className='heartIcon'  size={"25px"}/>
    <p>Wishlist</p>
   </div>
   </div>
</div>
{slideCart && <Cart setCartslide={setSlidecart}/>}
{authTile && <LoginPage setAuthtile={setAuthtile}/>}
</div>

  )
}

export default Header
