import "./Products.scss";
import Product from "./Product/Product"
const Products = ({headingText}) => {
    return <div className="products-layout">
        <div className="category-heading">{headingText}</div>
        <div className="product-cards">
        <Product/>
        <Product/>
        <Product/>
        <Product/>
        <Product/>
        <Product/>
        <Product/>
        <Product/>
        </div>
    </div>;
};

export default Products;
