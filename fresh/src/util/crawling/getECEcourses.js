import getBMcourses from "./getBMcourses.js";
import axios from "axios";
import cheerio from "cheerio";

export default async function getCShref() {
    try {
      // get all CS courses data from the website
      const url = "https://www.stonybrook.edu/sb/bulletin/current/courses/est/";
      const html = await axios.get(url);
      const $ = cheerio.load(html.data);
      const courseList = $("tbody tr");
   
      courseList.map((i, element)=>{
        let elem= $(element).find("div.course");

        //TODO
        let href = $(elem).attr("href");

        getBMcourses(href)
      })

    } catch (error) {
      console.error(error);
    }
     
  };

  //getBMhref(); //FOR TESTING