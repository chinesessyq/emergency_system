"use strict";(self["webpackChunkweb"]=self["webpackChunkweb"]||[]).push([[759],{85759:function(e,t,n){n.r(t),n.d(t,{default:function(){return d}});var a=function(){var e=this,t=e._self._c;return t("el-container",{staticClass:"home_container"},[t("el-header",[t("div",{staticClass:"home_title"},[e._v("应急系统")]),t("div",{staticClass:"home_userinfoContainer"},[t("el-dropdown",{on:{command:e.handleCommand}},[t("span",{staticClass:"el-dropdown-link home_userinfo"},[e._v(" "+e._s(e.currentUserName)),t("i",{staticClass:"el-icon-arrow-down el-icon--right home_userinfo"})]),t("el-dropdown-menu",[t("el-dropdown-item",{attrs:{command:"sysCfg"}},[e._v("系统管理")]),t("el-dropdown-item",{attrs:{command:"logout",divided:""}},[e._v("退出登录")])],1)],1)],1)]),t("el-container",[t("el-aside",{attrs:{width:"160px"}},[t("el-menu",{staticClass:"el-menu-vertical-demo",staticStyle:{"background-color":"#ececec"},attrs:{"default-active":"0",router:""},on:{open:e.handleOpen,close:e.handleClose}},[[t("el-menu-item",{attrs:{index:"/layout"}},[t("span",[e._v("home")])])],[t("el-menu-item",{attrs:{index:"/layout/data"}},[t("span",[e._v("data")])])],[t("el-menu-item",{attrs:{index:"/layout/equipment"}},[t("span",[e._v("equipment")])])]],2)],1),t("el-main",{staticStyle:{"padding-top":"10px","padding-left":"4px","padding-right":"4px"}},[t("router-view")],1)],1)],1)},i=[],o=n(63822),s={data(){return{currentUserName:"系统管理员",isAdmin:!0,isNormal:!0,hasUncheckedApplyPermission:!1,hasUncheckedApprovalPermission:!1,hasTagExceptionPermission:!1}},methods:{handleCommand(e){var t=this;"logout"==e&&this.$confirm("注销登录吗?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){t.currentUserName="游客",t.$router.replace({path:"/"})}))},...(0,o.nv)({selectLine:"selectLine",selectCircle:"selectCircle"})},created(){this.selectLine(localStorage.getItem("token")),this.selectCircle(localStorage.getItem("token"))},mounted:function(){var e=this;e.currentUserName="系统管理员"}},r=s,l=n(1001),c=(0,l.Z)(r,a,i,!1,null,"d39da68e",null),d=c.exports}}]);
//# sourceMappingURL=759.ec8504ae.js.map