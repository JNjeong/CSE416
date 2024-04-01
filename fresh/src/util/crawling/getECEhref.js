import getECEcourses from "./getECEcourses.js";
import axios from "axios";
import cheerio from "cheerio";

export default async function getECEhref() {
    try {
      // get all CS courses data from the website
      const url = "https://ece.sunykorea.ac.kr/ece/html/sub03/030101.html";
      const html = await axios.get(url);
      const $ = cheerio.load(html.data);
      const courseList = $("tbody tr");
   
      courseList.map((i, element)=>{
        let elem= $(element).find("td a.btn-default");
        let href = $(elem).attr("href");

        getECEcourses(href)
      })

    } catch (error) {
      console.error(error);
    }
     
  };

  getECEhref(); //FOR TESTING