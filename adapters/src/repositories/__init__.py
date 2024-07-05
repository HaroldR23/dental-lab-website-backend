from .email_sender import SMTPEmailSenderRepository
from .memory import (MemoryAppointmentRepository, MemoryEmailSenderRepository,
                     MemoryProductRepository)
from .sql import SQLAppointmentRepository, SQLProductRepository
