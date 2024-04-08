import "./Category.scss";
import Products from "../Products/Products";
const Category = () => {
    return <div className="category-page">
        <div className="product-section">
            <Products headingText="Category Heading"/>
        </div>
    </div>;
};

export default Category;
