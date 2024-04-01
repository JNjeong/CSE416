import getBMcourses from "./getBMcourses.js";
import axios from "axios";
import cheerio from "cheerio";

export default async function getCShref() {
    try {
      // get all CS courses data from the website
      const url = "https://bm.sunykorea.ac.kr/bm/html/sub03/030107.html";
      const html = await axios.get(url);
      const $ = cheerio.load(html.data);
      const courseList = $("tbody tr");
   
      courseList.map((i, element)=>{
        let elem= $(element).find("td a.btn-default");
        let href = $(elem).attr("href");

        getBMcourses(href)
      })

    } catch (error) {
      console.error(error);
    }
     
  };

  //getBMhref(); //FOR TESTING