import { Outlet } from "react-router-dom";
import ComponentOne from "../components/ComponentOne";

const LayoutOne = () => {
  return (
    <>
      <ComponentOne />
      <Outlet />
    </>
  );
};
export default LayoutOne;
