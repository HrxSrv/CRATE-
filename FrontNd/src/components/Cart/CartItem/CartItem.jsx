import React, { useContext } from "react";
import { MdClose } from "react-icons/md";
import prod from "../../../assets/products/watch-prod-2.webp";
import "./CartItem.scss";
const CartItem = () => {
  return (
    <div className="cart-products">
      <div className="cart-product">
        <div className="image-container">
          <img src={prod} />
        </div>
        <div className="prod-details">
          <span className="name">product-name</span>
          <div className="close-btn">
          <MdClose/>
          </div>
          <div className="quantity-buttons">
            <span >
              -
            </span>
            <span>2</span>
            <span>
              +
            </span>
          </div>
          <div className="text">
            <span>2</span>
            <span>x</span>
            <span className="highlight">
              <span>&#8377;</span>
              2500
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CartItem;
