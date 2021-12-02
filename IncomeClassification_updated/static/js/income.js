function getquerydata()
{
    const age = +document.getElementById("Age").value;
    const maritalstatus = document.getElementById("marital-status").value;
    const workclass = document.getElementById("Work Class").value;
    const race = document.getElementById("Race").value;
    const nativecountry = document.getElementById("native-country").value;
    const gender = document.getElementById("Gender").value;
    //const grade_level = document.getElementById("Education").value;
    const degree_type = document.getElementById("Education").value;
    const occupationType = document.getElementById("Occupation").value;
    const hoursPerWeek = +document.getElementById("Hours per week").value;
    const relationship = document.getElementById("Relationship").value;
    return {age,maritalstatus,workclass,race,nativecountry, gender,  degree_type, occupationType, hoursPerWeek,relationship}
}

function getResponse()
{
    console.log("Team 2 Rules")
    const data = getquerydata();
    fetch("/predict", {
        method: "POST",
        cache: "no-cache",
        body: JSON.stringify(data),
        headers: new Headers({
            "Content-Type": "application/json",
        })
    }).then(data=>data.text()).then(data=>{
        alert(data)
    })
}