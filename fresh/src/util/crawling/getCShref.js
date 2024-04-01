import getCScourses from "./getCScourses.js";
import axios from "axios";
import cheerio from "cheerio";

export default async function getCShref() {
    try {
      // get all CS courses data from the website
      const url = "https://cs.sunykorea.ac.kr/cs/html/sub03/030203.html";
      const html = await axios.get(url);
      const $ = cheerio.load(html.data);
      const courseList = $("tbody tr");
   
      courseList.map((i, element)=>{
        let elem= $(element).find("td a.code_btn");
        let href = $(elem).attr("href");

        getCScourses(href)
      })

    } catch (error) {
      console.error(error);
    }
     
  };

  //getCShref(); //FOR TESTING