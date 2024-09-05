import "./App.css";

import { Navigate, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import PageOne from "./pages/PageOne";
import PageTwo from "./pages/PageTwo";
import LayoutOne from "./layouts/LayoutOne";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<LayoutOne />}>
          <Route index element={<Home />}></Route>
          <Route path="page-one" element={<PageOne />}></Route>
          <Route path="page-two" element={<PageTwo />}></Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
