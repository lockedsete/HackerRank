read -n 1 stdin
# -n 1 -> A flag that restricts the input to exactly 1 character. The script moves forward immediately once a key is pressed, without waiting for the user to hit Enter
if [ "${stdin,,}" == "y" ]; then
    # stdin,, -> A Bash parameter expansion that converts the string to lowercase. This ensures that if the user types a capital "Y", it is still treated as "y".
    echo "YES"
else
    echo "NO"
fi
