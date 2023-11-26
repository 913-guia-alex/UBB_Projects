class GymMembership {
  final int id;
  final String firstName;
  final String lastName;
  final String email;
  final String creationDate;
  final String expirationDate;
  final String gymName;

  GymMembership({
    required this.id,
    required this.firstName,
    required this.lastName,
    required this.email,
    required this.creationDate,
    required this.expirationDate,
    required this.gymName,
  });

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
