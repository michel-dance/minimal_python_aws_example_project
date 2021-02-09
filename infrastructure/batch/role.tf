resource "aws_iam_role" "container" {

  name = "${var.name}-container"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

data "aws_iam_policy_document" "container" {

  statement {
    actions = [
      "s3:*"
    ]

    effect = "Allow"

    resources = [
      "arn:aws:s3:::*"
    ]
  }
}

resource "aws_iam_role_policy" "container" {
  role = aws_iam_role.container.name

  policy = data.aws_iam_policy_document.container.json
}