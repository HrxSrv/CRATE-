import "./SaleProduct.scss";
import pImg from "../../../assets/products/earbuds-prod-1.webp"
const SaleProduct = () => {
    return <div className="Sale-product">
        <img src={pImg} alt="" />
        <span className="details">Boat airdopes 299 | Enc | 24 hrs Backupasasdawdaswd</span>
        <span className="price"><span className="rupee">₹</span>499</span>
    </div>;
};

export default SaleProduct;
