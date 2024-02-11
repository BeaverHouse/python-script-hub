from string import Template

readme_query_template = Template(
    """{
        repository(owner: "$owner", name: "$name") {
            description 
            homepageUrl
        }
    }"""
)

overview_query_template = Template(
    """{
    repository(owner: "$owner", name: "$name") {
      name
      description
      isTemplate
      webCommitSignoffRequired
      defaultBranchRef {
        name
      }
      hasWikiEnabled
      hasIssuesEnabled
      isBlankIssuesEnabled
      hasDiscussionsEnabled
      hasProjectsEnabled
      mergeCommitAllowed
      squashMergeAllowed
      rebaseMergeAllowed
      allowUpdateBranch
      autoMergeAllowed
      deleteBranchOnMerge
      mergeCommitTitle
      mergeCommitMessage
      squashMergeCommitTitle
      squashMergeCommitMessage
      isArchived
      
      branchProtectionRules(first: 100) {
        nodes {
          pattern
          requiredApprovingReviewCount
          dismissesStaleReviews
          requiresCodeOwnerReviews
          restrictsReviewDismissals
          bypassPullRequestAllowances(first:1) {
            edges {
              node {
                id
              }
            }
          }
          requireLastPushApproval
          requiresStatusChecks
          requiresStrictStatusChecks
          requiredStatusChecks {
            context
          }
          requiresConversationResolution
          requiresCommitSignatures
          requiresLinearHistory
          requiresDeployments
          lockBranch
          isAdminEnforced
          pushAllowances(first:1) {
            edges {
              node {
                id
              }
            }
          }
          allowsForcePushes
          allowsDeletions
        }
      }
      rulesets(first: 1) {
        edges {
          node {
            name
          }
        }
      }
      hasVulnerabilityAlertsEnabled    
      labels(first: 100) {
        nodes {
          name
          color
        }
      }
      issues {
        totalCount
      }
    }
}"""
)