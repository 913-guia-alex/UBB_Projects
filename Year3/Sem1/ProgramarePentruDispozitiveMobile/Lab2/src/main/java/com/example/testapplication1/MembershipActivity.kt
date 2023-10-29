package com.example.testapplication1

import com.example.testapplication1.GymMembershipManager.generateNewMembershipId
import android.annotation.SuppressLint
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import java.text.SimpleDateFormat
import java.util.regex.Pattern


//Controller function
class MembershipActivity : ComponentActivity() {
    private lateinit var navController: NavHostController

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            val navHostController = rememberNavController()
            navController = navHostController

            NavHost(navController = navController, startDestination = "membershipList") {
                composable("membershipList") {
                    MembershipScreen(navController) {
                        navController.navigate("addMembership")
                    }
                }
                composable("addMembership") {
                    AddMembershipScreen(navController) {
                        navController.popBackStack()
                    }
                }
            }
        }
    }
}


//Function that generates the main screen for the user where he can see tha list of Memberships
@Composable
fun MembershipScreen(
    navController: NavController,
    navigateToAddScreen: () -> Unit
) {
    val memberships = remember { mutableStateOf(GymMembershipManager.getAllMemberships()) }
    val showDialog = remember { mutableStateOf(false) }
    var deleteMemberId by remember { mutableStateOf(-1) }
    var selectedMemberForUpdate by remember { mutableStateOf<GymMembership?>(null) }

    Surface(modifier = Modifier.fillMaxSize()) {
        Column {
            Text(text = "List of Gym Memberships:")
            memberships.value.forEach { membership ->
                MembershipItem(
                    membership,
                    onDelete = { memberId ->
                        showDialog.value = true
                        deleteMemberId = memberId
                    },
                    onUpdate = { membership ->
                        selectedMemberForUpdate = membership
                    }
                )
            }
            AddMembershipButton(navigateToAddScreen)
        }
    }

    if (showDialog.value) {
        showDeleteConfirmationDialog(deleteMemberId) { confirmed ->
            if (confirmed) {
                memberships.value = memberships.value.toMutableList().apply {
                    removeAll { it.id == deleteMemberId }
                }
                GymMembershipManager.deleteMembership(deleteMemberId)
            }
            showDialog.value = false
        }
    }

    selectedMemberForUpdate?.let { member ->
        UpdateMembershipScreen(member, navController) { updatedMembership ->
            if (isValidUpdate(updatedMembership)) {
                GymMembershipManager.updateMembership(updatedMembership)
                memberships.value = GymMembershipManager.getAllMemberships()
                navController.popBackStack()
            } else {
                // Handle validation errors or display an error message
            }
            selectedMemberForUpdate = null
        }
    }
}

//The function that handles the GymMembership object
@Composable
fun MembershipItem(
    membership: GymMembership,
    onDelete: (Int) -> Unit,
    onUpdate: (GymMembership) -> Unit
) {
    Column {
        Text("ID: ${membership.id}")
        Text("First Name: ${membership.firstName}")
        Text("Last Name: ${membership.lastName}")
        Text("Email: ${membership.email}")
        Text("Creation Date: ${membership.creationDate}")
        Text("Expiration Date: ${membership.expirationDate}")
        Text("Gym Name: ${membership.gymName}")


        Row {
            Button(onClick = { onDelete(membership.id) }) {
                Text("Delete")
            }

            Button(onClick = { onUpdate(membership) }) {
                Text("Update")
            }
        }
    }
}

//Function that creates the Add Membership Screen and uses the validations and messages to add an object
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddMembershipScreen(
    navController: NavController,
    onSubmit: () -> Unit
) {
    var firstName by remember { mutableStateOf("") }
    var lastName by remember { mutableStateOf("") }
    var email by remember { mutableStateOf("") }
    var creationDate by remember { mutableStateOf("") }
    var expirationDate by remember { mutableStateOf("") }
    var gymName by remember { mutableStateOf("") }

    val validationErrors = remember { mutableStateOf("") }

    Surface(modifier = Modifier.fillMaxSize()) {
        Column(
            modifier = Modifier.padding(16.dp)
        ) {
            TextField(
                value = firstName,
                onValueChange = { firstName = it },
                label = { Text("First Name") }
            )

            TextField(
                value = lastName,
                onValueChange = { lastName = it },
                label = { Text("Last Name") }
            )

            TextField(
                value = email,
                onValueChange = { email = it },
                label = { Text("Email") }
            )

            TextField(
                value = creationDate,
                onValueChange = { creationDate = it },
                label = { Text("Creation Date") }
            )

            TextField(
                value = expirationDate,
                onValueChange = { expirationDate = it },
                label = { Text("Expiration Date") }
            )

            TextField(
                value = gymName,
                onValueChange = { gymName = it },
                label = { Text("Gym Name") }
            )

            Button(
                onClick = {
                    val newMembership = GymMembership(
                        id = generateNewMembershipId(),
                        firstName = firstName,
                        lastName = lastName,
                        email = email,
                        creationDate = creationDate,
                        expirationDate = expirationDate,
                        gymName = gymName
                    )

                    val validationMessage = generateValidationMessage(newMembership)
                    if (validationMessage.isBlank()) {
                        GymMembershipManager.addMembership(newMembership)
                        onSubmit()
                    } else {
                        validationErrors.value = validationMessage
                    }
                },
                modifier = Modifier.padding(vertical = 16.dp)
            ) {
                Text("Submit")
            }

            if (validationErrors.value.isNotBlank()) {
                Text(
                    text = "Validation Error: ${validationErrors.value}",
                    color = Color.Red,
                    modifier = Modifier.padding(top = 8.dp)
                )
            }
        }
    }
}

//The function that handles the button for Add Membership
@Composable
fun AddMembershipButton(onAddMembershipClick: () -> Unit) {
    Button(onClick = onAddMembershipClick) {
        Text(text = "Add Membership")
    }
}

//Function that creates the Update Membership Screen and uses the validations and messages to update an object
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun UpdateMembershipScreen(
    membership: GymMembership,
    navController: NavController,
    onUpdate: (GymMembership) -> Unit
) {
    var firstName by remember { mutableStateOf(membership.firstName) }
    var lastName by remember { mutableStateOf(membership.lastName) }
    var email by remember { mutableStateOf(membership.email) }
    var creationDate by remember { mutableStateOf(membership.creationDate) }
    var expirationDate by remember { mutableStateOf(membership.expirationDate) }
    var gymName by remember { mutableStateOf(membership.gymName) }

    val validationErrors = remember { mutableStateOf("") }

    Surface(modifier = Modifier.fillMaxSize()) {
        Column(modifier = Modifier.padding(16.dp)) {
            TextField(
                value = firstName,
                onValueChange = { firstName = it },
                label = { Text("First Name") }
            )

            TextField(
                value = lastName,
                onValueChange = { lastName = it },
                label = { Text("Last Name") }
            )

            TextField(
                value = email,
                onValueChange = { email = it },
                label = { Text("Email") }
            )

            TextField(
                value = creationDate,
                onValueChange = { creationDate = it },
                label = { Text("Creation Date") }
            )

            TextField(
                value = expirationDate,
                onValueChange = { expirationDate = it },
                label = { Text("Expiration Date") }
            )

            TextField(
                value = gymName,
                onValueChange = { gymName = it },
                label = { Text("Gym Name") }
            )

            Button(
                onClick = {
                    val updatedMembership = membership.copy(
                        firstName = firstName,
                        lastName = lastName,
                        email = email,
                        creationDate = creationDate,
                        expirationDate = expirationDate,
                        gymName = gymName
                    )

                    val validationMessage = generateValidationMessage(updatedMembership)
                    if (validationMessage.isBlank()) {
                        onUpdate(updatedMembership)
                        navController.navigate("membershipList") // Navigate back to the list after updating
                    } else {
                        validationErrors.value = validationMessage
                    }
                },
                modifier = Modifier.padding(vertical = 16.dp)
            ) {
                Text("Update")
            }

            if (validationErrors.value.isNotBlank()) {
                Text(
                    text = "Validation Error: ${validationErrors.value}",
                    color = Color.Red,
                    modifier = Modifier.padding(top = 8.dp)
                )
            }
        }
    }
}

//Function that handles the Deletion of an object . Generates the Deletion dialog and the confirmation for deletion
@Composable
fun showDeleteConfirmationDialog(memberId: Int, onDeleteConfirmed: (Boolean) -> Unit) {
    AlertDialog(
        onDismissRequest = {
            onDeleteConfirmed(false)
        },
        title = { Text("Confirm Deletion") },
        text = { Text("Are you sure you want to delete this membership?") },
        confirmButton = {
            Button(onClick = {
                onDeleteConfirmed(true)
            }) {
                Text("Delete")
            }
        },
        dismissButton = {
            Button(onClick = {
                onDeleteConfirmed(false)
            }) {
                Text("Cancel")
            }
        }
    )
}


//Function that generates the error message for the Add and Update
fun generateValidationMessage(updatedMembership: GymMembership): String {
    val errorMessage = StringBuilder()

    // Validation for member name (only string characters)
    val namePattern: Pattern = Pattern.compile("^[a-zA-Z ]+\$")
    if (!namePattern.matcher(updatedMembership.firstName).matches()) {
        errorMessage.append("First Name is invalid. ")
    }
    if (!namePattern.matcher(updatedMembership.lastName).matches()) {
        errorMessage.append("Last Name is invalid. ")
    }

    // Validation for email
    if (!android.util.Patterns.EMAIL_ADDRESS.matcher(updatedMembership.email).matches()) {
        errorMessage.append("Email is invalid. ")
    }

    // Validation for date format (creation and expiration dates)
    val dateFormat: SimpleDateFormat = SimpleDateFormat("yyyy-MM-dd")
    dateFormat.isLenient = false

    try {
        dateFormat.parse(updatedMembership.creationDate)
    } catch (e: Exception) {
        errorMessage.append("Creation Date is invalid. ")
    }

    try {
        dateFormat.parse(updatedMembership.expirationDate)
    } catch (e: Exception) {
        errorMessage.append("Expiration Date is invalid. ")
    }

    return errorMessage.toString()
}


//Validation function for Add and Update
@SuppressLint("SimpleDateFormat")
fun isValidUpdate(updatedMembership: GymMembership): Boolean {
    // Validation for first and last name (only string characters)
    val namePattern: Pattern = Pattern.compile("^[a-zA-Z ]+\$")
    val isFirstAndLastNameValid: Boolean =
        namePattern.matcher(updatedMembership.firstName).matches() &&
                namePattern.matcher(updatedMembership.lastName).matches()

    // Validation for email
    val emailPattern: Pattern = Pattern.compile("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\$")
    val isEmailValid: Boolean = emailPattern.matcher(updatedMembership.email).matches()

    // Validation for date format (creation and expiration dates)
    val dateFormat: SimpleDateFormat = SimpleDateFormat("yyyy-MM-dd")
    dateFormat.isLenient = false

    var isCreationDateValid = true
    var isExpirationDateValid = true

    try {
        dateFormat.parse(updatedMembership.creationDate)
    } catch (e: Exception) {
        isCreationDateValid = false
    }

    try {
        dateFormat.parse(updatedMembership.expirationDate)
    } catch (e: Exception) {
        isExpirationDateValid = false
    }

    // Return true only if all validations pass
    return isFirstAndLastNameValid && isEmailValid && isCreationDateValid && isExpirationDateValid
}

//The main function of our program
@Preview
@Composable
fun MembershipPreview() {
    val memberships = GymMembershipManager.getAllMemberships()
    Surface {
        Column {
            Text(text = "List of Gym Memberships:")
            memberships.forEach { membership ->
                MembershipItem(
                    membership,
                    onDelete = {},
                    onUpdate = {}
                )
            }
        }
    }
}