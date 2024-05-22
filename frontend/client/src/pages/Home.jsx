import React from "react";
import Createpost from "./Create-post";
import MyComponent from "./Create-post";
import ListAllPost from "./List-All-Posts";
import UpdatePost from "./Update";

export default function Home() {

  
  return <div className="text-center">Home
  
    <Createpost/>
    <ListAllPost/>
    {/* <UpdatePost/> */}
  </div>;
}
