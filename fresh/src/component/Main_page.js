import "../css/main_page_style.css";
// import "../css/animation.css";
import stonybrook_logo from '../image/stonybrook_logo.png';
import runAnimations, { allLinks, allFunctions } from "../js/main_page_script";
import React, { useEffect } from 'react';
const Main_page = () => {
  useEffect(() => {
    runAnimations();
  }, []);
  return (
    <div className="parent-div">
      <div className="header-87-1-307200 pos-abs" id="id-28344">
        <div className="stonybrooklogo pos-abs">
            <img src={stonybrook_logo} className="logo-size" />
        </div>
        <div className="image-151-1-88230 pos-abs" id="id-1224163">
          <div
            className="nodeBg-1224163 pos-abs image-div bg-no-repeat  bg-crop"
            id="id-bg-1224163"
          >
            {" "}
          </div>
        </div>
        <div className="next-generation-1-24674 pos-abs" id="id-1224140">
          <span className="next-generation-1-24674-0">
            {"Next generation "}&nbsp;{""} <br /> {" website builder"}
          </span>
        </div>
        <div className="greate-websites-1-12492 pos-abs" id="id-1224141">
          <span className="greate-websites-1-12492-0">
            {"Greate websites with new technology — not with the old one"}
          </span>
        </div>
        <div className="buttonlogin-1-3176-container pos-abs" id="id-1224137">
          <div className="buttonlogin-1-289083 pos-abs" id="id-1224137">
            <div className="log-in-1-749427 pos-abs" id="id-I1224137_5131">
              <span className="log-in-1-749427-0">{"Login"}</span>
            </div>
          </div>
        </div>
        <div className="buttonlogin-2-145905-container pos-abs" id="id-1224138">
          <div className="buttonlogin-1-501120 pos-abs" id="id-1224138">
            <div className="log-in-1-153333 pos-abs" id="id-I1224138_5131">
              <span className="log-in-1-153333-0">{"Sing Up"}</span>
            </div>
          </div>
        </div>
        <div
          className="buttonstarted-1-217360-container pos-abs"
          id="id-1224139"
        >
          <div className="buttonstarted-1-82622 pos-abs" id="id-1224139">
            <div
              className="get-started-1-18456 pos-abs"
              id="id-I1224139_641163"
            >
              <span className="get-started-1-18456-0">
                {"Get started for free"}
              </span>
            </div>
          </div>
        </div>
        <div
          className="buttonstarted-2-155946-container pos-abs"
          id="id-1224158"
        >
          <div className="buttonstarted-1-386400 pos-abs" id="id-1224158">
            <div
              className="get-started-1-43152 pos-abs"
              id="id-I1224158_641163"
            >
              <span className="get-started-1-43152-0">
                {"order custom website"}
              </span>
            </div>
          </div>
        </div>
        <div className="sitelogo-1-187248-container pos-abs" id="id-1224135">
          <div className="sitelogo-1-472059 pos-abs" id="id-1224135">
            {/* <div
              className="line-3-1-480216 pos-abs"
              id="id-I1224135_1092824"
            ></div>
            <div
              className="line-4-1-120495 pos-abs"
              id="id-I1224135_1093000"
            ></div>
            <div
              className="line-5-1-140094 pos-abs"
              id="id-I1224135_1093201"
            ></div> */}
            <div className="sitelogo-1-204350 pos-abs" id="id-I1224135_153">
              <span className="sitelogo-1-204350-0">{"SUNY"}</span>
              <span className="sitelogo-1-204350-1">{"Korea"}</span>
            </div>
          </div>
        </div>
        <div className="menu-1-277764-container pos-abs" id="id-1224136">
          <div className="menu-1-797424 pos-abs" id="id-1224136">
            <div className="about-1-51192 pos-abs" id="id-I1224136_8215">
              <span className="about-1-51192-0">{"Location"}</span>
            </div>
            <div className="features-1-10700 pos-abs" id="id-I1224136_8216">
              <span className="features-1-10700-0">{"Weekly Schedule"}</span>
            </div>
            <div className="pricing-1-267960 pos-abs" id="id-I1224136_8217">
              <span className="pricing-1-267960-0">{"My Semester"}</span>
            </div>
            <div className="gallery-1-204248 pos-abs" id="id-I1224136_8218">
              <span className="gallery-1-204248-0">{"Website URL"}</span>
            </div>
            <div className="team-1-42096 pos-abs" id="id-I1224136_8219">
              <span className="team-1-42096-0">{"Calender"}</span>
            </div>
          </div>
        </div>
        <div className="arrows-1-210330-container pos-abs" id="id-1224165">
          <div className="arrows-1-769934 pos-abs" id="id-1224165">
            <div className="pos-abs" id="id-I1224165_8187">
              <div
                className="nodeBg-I1224165_8187 pos-abs pos-init fill-parent bg-contain bg-no-repeat image-div"
                id="id-bg-I1224165_8187"
              ></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Main_page;