import logo from './logo.svg';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import React, { useState,useEffect} from "react";
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';
import Register from './customer/Register';
import Login from './customer/Login';
import AddProduct from './customer/AddProduct';
import UserList from './customer/UserList';
import AddToCart from './customer/AddToCart';
import HomePage from './admin/HomePage';
import ProductList from './customer/ProductList';
import AddSubCategory from './customer/AddSubCategory';
import AddCategory from './customer/AddCategory';
import Profile from './customer/Profile';
import Brand from './customer/Brand';
import Order from './customer/Order';
// import Protected from './Protected';
import Dashboard from './customer/Dashboard';
import AdminDash from './customer/AdminDash';
import ProductDetail from './components/productDetail';
import AllProduct from './customer/AllProduct';
import Wishlist from './components/wishlist';
import OrderDetails from './customer/OrderDetail';
// import AddToCart from './customer/AddToCart';
// import Cart from './CartComponent/Cart';
function App() {
  
  const [isAdmin, setRole]=useState();
  // const [isLoggedIn, setLogin] = useState();
  useEffect(() => {
    // if (localStorage.getItem("userName") !== null) {
    //   setLogin(true);
    // } else {
    //   setLogin(false);
    // }
  if(localStorage.getItem("role") ==="admin"){
    setRole(true);
  }else{
    setRole(false);
  }
  // console.log(localStorage.getItem("role"));
},[])
  return (
    <> 
      
        <Header />  
        <Routes> 
          {
            localStorage.getItem("role") === "admin" ?
            <>
            <Route path='/customer/UserList' element={<UserList />} />
            <Route path='/customer/ProductList' element={<ProductList />} />
            <Route path='/customer/Order' element={<Order />} />
            <Route path='/customer/OrderDetails/:id' element={<OrderDetails />} />
            <Route path='/customer/Dashboard' element={<Dashboard />} />
            <Route path='/customer/Brand' element={<Brand />} />
            <Route path='/customer/Profile' element={<Profile />} />
            <Route path='/customer/AddProduct' element={<AddProduct />} /> 
            <Route path='/AllProduct' element={<AllProduct />} />
            <Route path='/admin/HomePage' element={<HomePage />} />
            <Route path='/customer/AddSubCategory' element={<AddSubCategory />} />
            <Route path='/customer/AddCategory' element={<AddCategory />} />
            <Route path='/home' element={<Home />} />
            <Route path='*' element={<Home />} />
            <Route path='product/:product_slug/:product_id' element={<ProductDetail/>}/>
            <Route path='/customer/AdminDash' element={<AdminDash />} />
            <Route path='/components/wishlist' element={<Wishlist />} />
            <Route path='/customer/AddToCart' element={<AddToCart />} />
            </>
            : 
            <>
            <Route path='/customer/Register' element={<Register />} />
            <Route path='/customer/Profile' element={<Profile />} />
            <Route path='*' element={<Home />} />
            <Route path='/home' element={<Home />} />
            <Route path='/AllProduct' element={<AllProduct />} />
            <Route path='product/:product_slug/:product_id' element={<ProductDetail/>}/>
            <Route path='/customer/Login' element={<Login />} />
            <Route path='/components/wishlist' element={<Wishlist />} />
            <Route path='/customer/AddToCart' element={<AddToCart />} />

            </>
         }       
            
        </Routes> 
        <Footer /> 
     
    </>
  );
}
export default App;
