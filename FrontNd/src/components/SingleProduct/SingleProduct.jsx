import "./SingleProduct.scss";
import { BsFillCartPlusFill } from "react-icons/bs";
import {
  AiFillTwitterCircle,
  AiOutlineInstagram,
  AiOutlineWhatsApp,
} from "react-icons/ai";
import { BsMeta } from "react-icons/bs";
import Img from "../../assets/products/headphone-prod-1.webp";
import RelatedProducts from "./RelatedProducts/RelatedProducts"
const SingleProduct = () => {
  return (
    <div className="layout">
      <div className="top">
        <div className="left">
          <img src={Img} alt="" />
        </div>
        <div className="right">
          <div className="title">Boat Wonder Womens</div>
          <div className="details">
            The BOAT Wonder Women headphones offer powerful sound with 40mm
            drivers, long battery life, voice assistant support, and a stylish
            Wonder Woman design, making them ideal for music enthusiasts.
          </div>
          <div className="price">
            <span className="L-Rate">L-RATE</span>
            <span className="rupee">₹ 499</span>
          </div>
          <div className="buttons">
            <div className="count-button">
              <button className="changeBtn">-</button>
              <span>9</span>
              <button className="changeBtn">+</button>
            </div>
            <div className="a2c-button">
              <BsFillCartPlusFill />
              <span>ADD TO CART</span>
            </div>
          </div>
          <div className="category">
            <span>Category: </span>
            <p>Headphones</p>
          </div>
          <div className="share-buttons">
            <span>Share: </span>
            <div className="icon">
              <AiFillTwitterCircle size={"25px"} />
              <BsMeta size={"25px"} />
              <AiOutlineWhatsApp size={"25px"} />
              <AiOutlineInstagram size={"25px"} />
            </div>
          </div>
          <div className="divider-line"></div>
        </div>
      </div>
      <div className="bottom">
        <RelatedProducts/>
      </div>
    </div>
  );
};

export default SingleProduct;
