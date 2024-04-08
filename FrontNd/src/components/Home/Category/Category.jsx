import "./Category.scss";
import Cat1 from "../../../assets/category/cat-1.jpg";
const Category = () => {
    return <div className="categories">
        <div className="product-template">
          <img src={Cat1} alt="" />
        </div>
        <div className="product-template">
          <img src={Cat1} alt="" />
        </div>
        <div className="product-template">
          <img src={Cat1} alt="" />
        </div>
        <div className="product-template">
          <img src={Cat1} alt="" />
        </div>
    </div>;
};

export default Category;
