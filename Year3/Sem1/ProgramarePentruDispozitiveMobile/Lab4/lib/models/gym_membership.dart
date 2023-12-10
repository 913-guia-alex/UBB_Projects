class GymMembership {
  final int id;
  final String firstName;
  final String lastName;
  final String email;
  final String creationDate;
  final String expirationDate;
  final String gymName;

  GymMembership({
    required this.id, // Add this line to the constructor
    required this.firstName,
    required this.lastName,
    required this.email,
    required this.creationDate,
    required this.expirationDate,
    required this.gymName,
  });



  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'firstName': firstName,
      'lastName': lastName,
      'email': email,
      'creationDate': creationDate,
      'expirationDate': expirationDate,
      'gymName': gymName,
    };
  }

  factory GymMembership.fromMap(Map<String, dynamic> map) {
    return GymMembership(
      id: map['id'],
      firstName: map['firstName'],
      lastName: map['lastName'],
      email: map['email'],
      creationDate: map['creationDate'],
      expirationDate: map['expirationDate'],
      gymName: map['gymName'],
    );
  }

  // Add copyWith method
  GymMembership copyWith({
    int? id,
    String? firstName,
    String? lastName,
    String? email,
    String? creationDate,
    String? expirationDate,
    String? gymName,
  }) {
    return GymMembership(
      id: id ?? this.id,
      firstName: firstName ?? this.firstName,
      lastName: lastName ?? this.lastName,
      email: email ?? this.email,
      creationDate: creationDate ?? this.creationDate,
      expirationDate: expirationDate ?? this.expirationDate,
      gymName: gymName ?? this.gymName,
    );
  }

}
