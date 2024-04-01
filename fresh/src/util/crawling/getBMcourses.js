import axios from "axios";
import cheerio from "cheerio";

 export default async function getBMcourses(href) {
    const res = [];
    try {

      // get all CS courses data from the website
      const url = "https://bm.sunykorea.ac.kr/bm/html/sub03/030107.html";


      let CSurl = url+href;
      let CShtml = await axios.get(CSurl);
      let $ = cheerio.load(CShtml.data);

      const coursenamecredit = $("strong.title").text();
      const coursename = coursenamecredit.split("/")[0].split(":")[1];
      
      const credits = coursenamecredit.split("/")[1].split(":")[1];
      
      const coursefullname = $("strong.h-box").text();
      
      let detail = $("ul.info_list li").text();

      console.log("detail : ", detail);
      console.log("==============================================")
   
      return [coursename, coursefullname, credits, detail];

    } catch (error) {
      console.error(error);
    }

     
  };

