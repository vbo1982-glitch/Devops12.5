module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.8.5"

  cluster_name    = "devops-final-cluster"
  cluster_version = "1.31"

  vpc_id                         = module.vpc.vpc_id
  subnet_ids                     = module.vpc.private_subnets
  cluster_endpoint_public_access = true
  

  enable_cluster_creator_admin_permissions = true

  eks_managed_node_groups = {
    main_node = {
      min_size     = 2
      max_size     = 4
      desired_size = 4

      instance_types = ["t3.micro"]
      capacity_type  = "SPOT"
    }
  }
}