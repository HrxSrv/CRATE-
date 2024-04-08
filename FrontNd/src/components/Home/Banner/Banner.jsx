import "./Banner.scss";
const Banner = () => {
  return (
    <div>
      <div className="content">
        <img src={require("../../../assets/banner-img.png")} className="hero-img" alt="" />
        <div className="text-content">
          <h1>L-RATES</h1>
          <p>
            Crate gives you L-RATES, the lowest price on the internet for
            your product, ensuring you always secure the best deals available.
          </p>
          <div className="ctas">
          <div className="btn">
                    <div class="hover"></div>
                    <span>READ MORE</span>
        </div>
        <div className="btn">
                    <div class="hover"></div>
                    <span>DISCOVER</span>
        </div>
          </div>
        </div>
        </div>
      </div>
    
  );
};

export default Banner;
