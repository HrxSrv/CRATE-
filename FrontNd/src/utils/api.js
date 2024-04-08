import axios from "axios";
const def = {
  headers: {
    authorization: "bearer" + process.env.React_App_Stripe_App_Key,
  },
};
export const fetchDataFromApi = async (url) => {
  try {
    const { data } = await axios.get(process.env.BaseUrl + url, def);
    return data;
  } catch (error) {
    console.log(error);
    return error;
  }
};
