import "./Search.scss";
import { AiOutlineSearch } from "react-icons/ai";
const Search = () => {
    return (
        <div className="search">
        <input type='text' placeholder='Search Your Product' autoComplete='off'></input>
        <AiOutlineSearch size={"50px"} className='searchIcon'/>
    </div>
    );
};

export default Search;
