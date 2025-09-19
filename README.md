# BNZFS Membership Management System

A modern, secure membership management system for Bangladesh New Zealand Friendship Society Inc. (BNZFS) built with Next.js, FastAPI, and AWS serverless architecture.

## Project Overview

**Organization**: Bangladesh New Zealand Friendship Society Inc.  
**Purpose**: Digital transformation of membership management with secure payment processing  
**Members**: ~200 active members in New Zealand  
**Membership Cycle**: July to June annually (e.g., 2024-25, 2023-24)

## Key Features

### Phase 1: Authentication & Member Portal
- Mobile-based OTP authentication (SMS via AWS SNS)
- Secure member dashboard showing payment history
- Outstanding dues calculation and tracking
- Special warnings for members with 3+ consecutive unpaid years

### Phase 2: Payment Integration
- POLi payment gateway integration for NZ bank transfers
- Automated payment processing and confirmation
- Real-time Google Sheets updates
- SMS/Email payment confirmations

### Phase 3: Admin Management
- Comprehensive admin dashboard
- Member management and delinquent tracking
- Annual fee setup and bulk operations
- Automated reminder system

### Phase 4: Notification System
- SMS notifications for OTP, payments, and reminders
- Email notifications for members with email addresses
- Automated payment reminder workflows
- Admin alerts and system notifications

## Technology Stack

### Frontend
- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Query + Zustand
- **Authentication**: Custom JWT implementation

### Backend
- **API Framework**: FastAPI (Python 3.11)
- **Authentication**: JWT + OTP via SMS
- **Database**: Google Sheets API integration
- **Payments**: POLi REST API
- **Background Tasks**: AWS Lambda functions

### AWS Services
- **Compute**: Lambda Functions (serverless)
- **API Management**: API Gateway
- **Content Delivery**: CloudFront + S3
- **Messaging**: SNS for SMS delivery
- **Security**: Systems Manager for secrets
- **Monitoring**: CloudWatch

### External Integrations
- **Google Sheets API**: Member data and payment records
- **POLi Payments**: New Zealand bank transfer gateway
- **AWS SNS**: SMS OTP and notifications to NZ mobile numbers

## Architecture
```bash
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐    ┌──────────────────┐
│   Members   │───▶│  CloudFront  │───▶│   API Gateway   │───▶│ Lambda Functions │
│ (NZ Mobile) │    │   (CDN/SSL)  │    │  (REST API)     │    │   (FastAPI)      │
└─────────────┘    └──────────────┘    └─────────────────┘    └──────────────────┘
                                                                        │
       ┌────────────────────────────────────────────────────────────────┼────────────┐
       │                                                                │            │
       ▼                                                                ▼            ▼
┌─────────────┐                                                 ┌──────────────┐ ┌─────────┐
│    AWS SNS  │                                                 │ Google Sheets│ │  POLi   │
│ (SMS to NZ) │                                                 │     API      │ │Payments │
└─────────────┘                                                 └──────────────┘ └─────────┘
```

## Project Structure
```bash
bnzfs-membership-system/
├── frontend/                   # Next.js application
│   ├── app/                   # App Router structure
│   ├── components/            # Reusable components
│   ├── lib/                   # Utilities and configurations
│   ├── types/                 # TypeScript type definitions
│   └── public/                # Static assets
├── backend/                   # FastAPI application
│   ├── app/
│   │   ├── api/              # API route handlers
│   │   ├── core/             # Core configuration
│   │   ├── models/           # Pydantic models
│   │   ├── services/         # Business logic
│   │   └── utils/            # Helper functions
│   ├── tests/                # API tests
│   └── requirements.txt      # Python dependencies
├── infrastructure/           # AWS CDK deployment
│   ├── lib/                  # CDK stack definitions
│   ├── bin/                  # CDK app entry point
│   └── cdk.json              # CDK configuration
├── docs/                     # Project documentation
│   ├── api/                  # API documentation
│   ├── deployment/           # Deployment guides
│   └── architecture/         # System architecture
└── .github/workflows/        # CI/CD pipeline
```
## Development Setup

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- AWS CLI configured
- Git

### Quick Start
```bash
# Clone the repository
git clone https://github.com/[your-username]/bnzfs-membership-system.git
cd bnzfs-membership-system

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start development servers
cd ../frontend && npm run dev    # Port 3000
cd ../backend && uvicorn app.main:app --reload    # Port 8000
```

## Security Features

- JWT-based authentication with 24-hour expiry
- OTP codes with 10-minute expiry and SMS delivery
- HTTPS encryption for all communications
- Input validation and sanitisation
- AWS IAM role-based access control
- PCI compliance through POLi payment gateway

## Contributing

### Development Workflow
1. Fork the repository
2. Create feature branch: `git checkout -b feature/feature-name`
3. Commit changes: `git commit -m 'Add feature description'`
4. Push to branch: `git push origin feature/feature-name`
5. Submit pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.
