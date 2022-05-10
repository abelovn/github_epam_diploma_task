resource "aws_docdb_cluster" "docdb" {
  cluster_identifier      = "my-docdb-cluster"
  engine                  = "docdb"
  master_username         = var.dbuser
  master_password         = var.dbpass
  backup_retention_period = 5
  preferred_backup_window = "01:00-02:00"
  skip_final_snapshot     = true
  db_subnet_group_name    = aws_db_subnet_group.abelovn-net-gr.name
  vpc_security_group_ids  = [aws_security_group.worker_group.id]
}

resource "aws_docdb_cluster_instance" "cluster_instances" {
  count              = 1
  identifier         = "docdb-cluster-abelovn-${count.index}"
  cluster_identifier = aws_docdb_cluster.docdb.id
  instance_class     = "db.t3.medium"
}
