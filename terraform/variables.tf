#------------------
#Key Pair Variables
#------------------
variable "ssh_ip" {
  type        = string
  description = "Set the ssh ip address"
}

variable "ssh_public_key" {
  type        = string
  description = "Set ssh public key"
}
