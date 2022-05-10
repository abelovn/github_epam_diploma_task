resource "aws_efs_file_system" "abelovn_nfs" {
   performance_mode = "generalPurpose"
}


resource "aws_efs_mount_target" "abelovn_nfs_mp-a" {
   file_system_id  = "${aws_efs_file_system.abelovn_nfs.id}"
   subnet_id = "${element(module.vpc.public_subnets, 0)}"
}

resource "aws_efs_mount_target" "abelovn_nfs_mp-b" {
   file_system_id  = "${aws_efs_file_system.abelovn_nfs.id}"
   subnet_id = "${element(module.vpc.public_subnets, 1)}"
}

resource "aws_efs_mount_target" "abelovn_nfs_mp-c" {
   file_system_id  = "${aws_efs_file_system.abelovn_nfs.id}"
   subnet_id = "${element(module.vpc.public_subnets, 2)}"
}