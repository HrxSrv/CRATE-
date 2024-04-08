import "./Home.scss";
import Banner from "./Banner/Banner"
import Category from './Category/Category'
import SaleProducts from "../SaleProducts/SaleProducts";
import { fetchDataFromApi } from "../../utils/api";
import { useEffect } from "react";
const Home = () => {
    // useEffect(()=>{
    //     getCategories()
    // },[])
    // const getCategories = ()=>{
    //      fetchDataFromApi("/api/products").then((res)=>console.log(res));
    // }
    
    return (<div className="home">
        <Banner/>
        <div className="show-items-by-cat">
        <Category/>
        </div>
        <SaleProducts headingText={"ALL TIME LOWEST"}/>
    </div>)
};

export default Home;
