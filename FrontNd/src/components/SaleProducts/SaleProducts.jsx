import "./SaleProducts.scss";
import SaleProduct from "./SaleProduct/SaleProduct"
const SaleProducts = ({headingText}) => {
    return <div className="Sale-products-layout">
        <div className="category-heading">
            {headingText}
        </div>
        <div className="Sale-product-cards">
        <SaleProduct/>
        <SaleProduct/>
        <SaleProduct/>
        <SaleProduct/>
        <SaleProduct/>
        <SaleProduct/>
        <SaleProduct/>
        <SaleProduct/>
        </div>
    </div>;
};

export default SaleProducts;
