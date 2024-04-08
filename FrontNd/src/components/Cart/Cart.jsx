import "./Cart.scss";
import { BsCartX } from "react-icons/bs";
import CartItem from "./CartItem/CartItem";
const Cart = ({ setCartslide }) => {
  return (
    <div className="cart-layout">
      <div className="opaque-layer"></div>
      <div className="cart-layer">
        <div className="header">
          <span>Shopping Cart</span>
          <div
            className="close-button"
            onClick={() => setCartslide((x) => !x)}
          ></div>
        </div>
        {/* <div className="empty-cart">
          <BsCartX />
          <p>Nothing in here !</p>
          <span>Return To Shopping</span>
        </div> */}
        <>
          <div className="cart-items">
          <CartItem/>
          <CartItem/>
          <CartItem/>
          <CartItem/>
          <CartItem/>
          <CartItem/>
          </div>
          <div className="cart-footer">
            <div className="subtotal">
              <span className="text">Subtotal:</span>
              <span className="text total">&#8377;12234</span>
            </div>
            <div className="button">
              <button className="checkout-cta">Checkout</button>
            </div>
          </div>
        </>
      </div>
    </div>
  );
};

export default Cart;
