<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ACT 2 Class Schedule</title>
</head>
<body>
    <?php
        $selectedDay = isset($_GET['day']) ? $_GET['day'] : '';
    ?>
    
    <form action="fetch-data.php" method="get">
        <label for="day">Day: </label>
        <select name="day" id="day" onchange="this.form.submit()">
            <option value="" <?= $selectedDay ? '' : 'selected' ?> disabled>Choose...</option>
            <option value="Monday" <?= $selectedDay == "Monday" ? 'selected' : '' ?>>Monday</option>
            <option value="Tuesday" <?= $selectedDay == "Tuesday" ? 'selected' : '' ?>>Tuesday</option>
            <option value="Wednesday" <?= $selectedDay == "Wednesday" ? 'selected' : '' ?>>Wednesday</option>
            <option value="Thursday" <?= $selectedDay == "Thursday" ? 'selected' : '' ?>>Thursday</option>
            <option value="Friday" <?= $selectedDay == "Friday" ? 'selected' : '' ?>>Friday</option>
            <option value="Saturday" <?= $selectedDay == "Saturday" ? 'selected' : '' ?>>Saturday</option>
        </select>
    </form>

    <br>

    <?php
        // Update this using your real schedule
        // Please list down the complete title of the subject
        $subjects = [
            ['subject' => '- Pagtuturo at Pagtataya sa Pagbasa at Pagsulat', 'day' => 'Monday'],
            ['subject' => '- PE 3: Individual and Dual Sports', 'day' => 'Monday'],
            ['subject' => '- Contemporary World', 'day' => 'Monday'],
            ['subject' => '- Web Applications Development 1', 'day' => 'Monday'],
            ['subject' => '- Organization and Management', 'day' => 'Tuesday'],
            ['subject' => '- Pagtuturo at Pagtataya sa Pagbasa at Pagsulat', 'day' => 'Tuesday'],
            ['subject' => '- Christian Teachings', 'day' => 'Tuesday'],
            ['subject' => '- Life and Works of Rizal', 'day' => 'Tuesday'],
            ['subject' => '- Contemporary World', 'day' => 'Wednesday'],
            ['subject' => '- Responsive Web Design', 'day' => 'Wednesday'],
            ['subject' => '- Web Applications and Development', 'day' => 'Thursday'],
            ['subject' => '- Data Structures and Algorithm', 'day' => 'Thursday'],
            ['subject' => '- Life and Works of Rizal', 'day' => 'Friday'],
            ['subject' => '- PE 3: Individual and Dual Sports', 'day' => 'Friday'],
            ['subject' => '- Christian Teachings', 'day' => 'Friday'],
            ['subject' => '- Web Applications and Development', 'day' => 'Friday'],
            ['subject' => '- Data Structures and Algorithm', 'day' => 'Saturday'],
            ['subject' => '- IS Infrastructure and Network Technologies', 'day' => 'Saturday'],
        ];

        switch ($selectedDay) {
            case "Monday":
                echo "Your subjects on Monday are:<br>";
                foreach ($subjects as $i) {
                    if ($i["day"] == $selectedDay) 
                    {
                        echo "{$i["subject"]}<br>"; 
                    }                
                }
                break;

            case "Tuesday":
                echo "Your subjects on Tuesday are:<br>";
                foreach ($subjects as $i) {
                    if ($i["day"] == $selectedDay)   
                    {
                        echo " ", "{$i["subject"]}<br>"; 
                    }                
                }
                break;

            case "Wednesday":
                echo "Your subjects on Wednesday are:<br>";
                foreach ($subjects as $i) {
                    if ($i["day"] == $selectedDay) 
                    {
                        echo " ", "{$i["subject"]}<br>"; 
                    }                
                }
                break;

            case "Thursday":
                echo "Your subjects on Thursday are:<br>";
                foreach ($subjects as $i) {
                    if ($i["day"] == $selectedDay) 
                    {
                        echo " ", "{$i["subject"]}<br>"; 
                    }                
                }
                break;

            case "Friday":
                echo "Your subjects on Friday are:<br>";
                foreach ($subjects as $i) {
                    if ($i["day"] == $selectedDay) 
                    {
                        echo " ", "{$i["subject"]}<br>"; 
                    }                
                }
                break;

            case "Saturday":
                echo "Your subjects on Saturday are:<br>";
                foreach ($subjects as $i) {
                    if ($i["day"] == $selectedDay) 
                    {
                        echo " ", "{$i["subject"]}<br>"; 
                    }                
                }
                break;

            default:
                echo "Please select a day.";
        }
    ?>
</body>
</html>