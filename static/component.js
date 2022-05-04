class Navbar extends HTMLElement{
    connectedCallback(){
        this.innerHTML=`
        <div class="container">
            <nav class="navbar navbar-expand-sm bg-primary text-white navbar-light fixed-top">
                <!-- Brand/logo -->
                <a class="navbar-brand">
                    UCSF Speech App
                </a>
                 
                <button class="navbar-toggler" type="button" data-toggle="collapse"
                            data-target="#collapse_Navbar">
                    <span class="navbar-toggler-icon"></span>
                </button>
                 
                <div class="collapse navbar-collapse justify-content-end" id="collapse_Navbar">
                    <ul class="navbar-nav">
                     
                        <li class="nav-item">
                            <a class="nav-link" href="#">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" class="bi bi-person-circle" viewBox="0 0 16 16">
                                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                                  </svg>
                            </a>
                        </li>
                     
                        <li class="nav-item">
                            <a class="nav-link" href="/logout">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
                                    <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
                                    <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
                                  </svg>
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
        `
    }
}

class ExpertMenu extends HTMLElement{
    connectedCallback(){
        this.innerHTML=`
        <head>
            <link href="/static/css/expertMenu.css" rel="stylesheet" type="text/css">
        </head?>
        <div class="menubar">
            <div class="menubar-wrapper"> 
                <div class="menubar-box">
                    <h3 class="menu-title"> Dashboard</h3>
                    <ul class="menu-list">
                        <li class="menu-list-item">
                                <a class="menu-icon" href="/expertPortal">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#1A1B41" class="bi bi-house-fill" viewBox="0 0 16 16">
                                    <path fill-rule="evenodd" d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                                    <path fill-rule="evenodd" d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z"/>
                                    </svg>
                                </a>
                                <a href="/expertPortal" style="text-decoration:none;">
                                    <h3 class="icon-titles">Home</h3>  
                                </a>
                        </li>
                        <li class="menu-list-item">
                            <a class="menu-icon" href="/expertPortal/createPrompt">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#1A1B41" class="bi bi-card-text" viewBox="0 0 16 16">
                                <path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h13zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13z"/>
                                <path d="M3 5.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 8a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 8zm0 2.5a.5.5 0 0 1 .5-.5h6a.5.5 0 0 1 0 1h-6a.5.5 0 0 1-.5-.5z"/>
                                </svg>
                            </a>
                            <a href="/expertPortal/createPrompt" style="text-decoration:none;">
                                <h3 class="icon-titles">Prompts</h3>  
                            </a>
                        </li>
                        <li class="menu-list-item"> 
                            <a class="menu-icon" href="/promptList">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#1A1B41" class="bi bi-briefcase" viewBox="0 0 16 16">
                                    <path d="M6.5 1A1.5 1.5 0 0 0 5 2.5V3H1.5A1.5 1.5 0 0 0 0 4.5v8A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-8A1.5 1.5 0 0 0 14.5 3H11v-.5A1.5 1.5 0 0 0 9.5 1h-3zm0 1h3a.5.5 0 0 1 .5.5V3H6v-.5a.5.5 0 0 1 .5-.5zm1.886 6.914L15 7.151V12.5a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5V7.15l6.614 1.764a1.5 1.5 0 0 0 .772 0zM1.5 4h13a.5.5 0 0 1 .5.5v1.616L8.129 7.948a.5.5 0 0 1-.258 0L1 6.116V4.5a.5.5 0 0 1 .5-.5z"/>
                                </svg>
                            </a>
                           
                          <!-- <a href=" http://127.0.0.1:5000/expertPortal/list_patients" style="text-decoration:none;">-->
                            <a href="/promptList" style="text-decoration:none;">
                                <h3 class="icon-titles">Patients</h3>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
    
        </div>
        `
    }

}

class PatientMenu extends HTMLElement{
    connectedCallback(){
        this.innerHTML=`
        <head>
            <link href="/static/css/patientMenu.css" rel="stylesheet" type="text/css">
            
        </head?>
        <div class="menubar">
            <div class="menubar-wrapper"> 
                <div class="menubar-box">
                    <h3 class="menu-title"> Dashboard</h3>
                    <ul class="menu-list">
                        <li class="menu-list-item">
                            <a class="menu-icon" href="/patientPortal">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#1A1B41" class="bi bi-house-fill" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                                <path fill-rule="evenodd" d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z"/>
                                </svg>
                            </a>
                            <a href="/patientPortal" style="text-decoration:none;">
                                <h3 class="icon-titles">Home</h3>  
                            </a>
                        </li>
                        <li class="menu-list-item">
                            <a class="menu-icon" href="/patientTasks">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#1A1B41" class="bi bi-card-text" viewBox="0 0 16 16">
                                <path d="M14.5 3a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h13zm-13-1A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13z"/>
                                <path d="M3 5.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 8a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 8zm0 2.5a.5.5 0 0 1 .5-.5h6a.5.5 0 0 1 0 1h-6a.5.5 0 0 1-.5-.5z"/>
                                </svg>
                            </a>
                            <a href="/patientTasks" style="text-decoration:none;">
                                <h3 class="icon-titles">Prompts</h3>  
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
    
        </div>
        `
    }

}


customElements.define("app-navbar", Navbar);
customElements.define("expert-menu", ExpertMenu);
customElements.define("patient-menu", PatientMenu);