import "./Product.scss";
import pImg from "../../../assets/products/earbuds-prod-1.webp"
const Product = () => {
    return <div className="product">
        <div className="card">
        <img src={pImg} alt="" />
        </div>
        <span className="details">Boat airdopes 299 | Enc | 24 hrs Backupasasdawdaswd</span>
        <span className="price"><span className="rupee">₹</span>499</span>
    </div>;
};

export default Product;
