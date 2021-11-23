function getquerydata()
{
    const age = +document.getElementById("Age").value;
    const gender = document.getElementById("Gender").value;
    const grade_level = +document.getElementById("Grade Level").value;
    const degree_type = document.getElementById("Degree Type").value;
    const occupationType = document.getElementById("Occupation Type").value;
    const hoursPerWeek = +document.getElementById("Hours Per Week").value;
    return {age, gender, grade_level, degree_type, occupationType, hoursPerWeek}
}

function getResponse()
{
    console.log("Team 2 Rules")
    const data = getquerydata();
    fetch("/predict", {
        method: "POST",
        cache: "no-cache",
        body: JSON.stringify(data),
    }).then(data=>data.text()).then(data=>{
        alert(data)
    })
}