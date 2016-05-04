# Copyright (C) 2016 Mike Mattice
#
# This file is part of pyemvtlv.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# (1) Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# (2) Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the
# distribution.
#
# (3)The name of the author may not be used to
# endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
doftags = {
    'IssuerIdentificationNumber'                               : '42',
    'ApplicationDedicatedFileName'                             : '4F',
    'ApplicationLabel'                                         : '50',
    'Track2EquivalentData'                                     : '57',
    'ApplicationPrimaryAccountNumber'                          : '5A',
    'CardholderName'                                           : '5F20',
    'ApplicationExpirationDate'                                : '5F24',
    'IssuerCountryCode'                                        : '5F28',
    'TransactionCurrencyCode'                                  : '5F2A',
    'LanguagePreference'                                       : '5F2D',
    'ServiceCode'                                              : '5F30',
    'ApplicationPrimaryAccountNumberSequenceNumber'            : '5F34',
    'TransactionCurrencyExponent'                              : '5F36',
    'IssuerURL'                                                : '5F50',
    'InternationalBankAccountNumber'                           : '5F53',
    'BankIdentifierCode'                                       : '5F54',
    'IssuerCountryCodeAlpha2format'                            : '5F55',
    'IssuerCountryCodeAlpha3format'                            : '5F56',
    'AccountType'                                              : '5F57',
    'ApplicationTemplate'                                      : '61',
    'FileControlInformationTemplate'                           : '6F',
    'READRECORDResponseMessageTemplate'                        : '70',
    'IssuerScriptTemplate1'                                    : '71',
    'IssuerScriptTemplate2'                                    : '72',
    'DirectoryDiscretionaryTemplate'                           : '73',
    'ResponseMessageTemplateFormat2'                           : '77',
    'ResponseMessageTemplateFormat1'                           : '80',
    'AmountAuthorisedBinary'                                   : '81',
    'ApplicationInterchangeProfile'                            : '82',
    'CommandTemplate'                                          : '83',
    'DedicatedFileName'                                        : '84',
    'IssuerScriptCommand'                                      : '86',
    'ApplicationPriorityIndicator'                             : '87',
    'ShortFileIdentifier'                                      : '88',
    'AuthorisationCode'                                        : '89',
    'AuthorisationResponseCode'                                : '8A',
    'CardRiskManagementDataObjectList1'                        : '8C',
    'CardRiskManagementDataObjectList2'                        : '8D',
    'CardholderVerificationMethodList'                         : '8E',
    'CertificationAuthorityPublicKeyIndex'                     : '8F',
    'IssuerPublicKeyCertificate'                               : '90',
    'IssuerAuthenticationData'                                 : '91',
    'IssuerPublicKeyRemainder'                                 : '92',
    'SignedStaticApplicationData'                              : '93',
    'ApplicationFileLocator'                                   : '94',
    'TerminalVerificationResults'                              : '95',
    'TransactionCertificateDataObjectList'                     : '97',
    'TransactionCertificateHashValue'                          : '98',
    'TransactionPersonalIdentificationNumberData'              : '99',
    'TransactionDate'                                          : '9A',
    'TransactionStatusInformation'                             : '9B',
    'TransactionType'                                          : '9C',
    'DirectoryDefinitionFileName'                              : '9D',
    'AcquirerIdentifier'                                       : '9F01',
    'AmountAuthorised'                                         : '9F02',
    'AmountOther'                                              : '9F03',
    'AmountOtherBinary'                                        : '9F04',
    'ApplicationDiscretionaryData'                             : '9F05',
    'ApplicationIdentifier-terminal'                           : '9F06',
    'ApplicationUsageControl'                                  : '9F07',
    'ApplicationVersionNumberICC'                              : '9F08',
    'ApplicationVersionNumberTerminal'                         : '9F09',
    'CardholderNameExtended'                                   : '9F0B',
    'IssuerActionCode-Default'                                 : '9F0D',
    'IssuerActionCode-Denial'                                  : '9F0E',
    'IssuerActionCode-Online'                                  : '9F0F',
    'IssuerApplicationData'                                    : '9F10',
    'IssuerCodeTableIndex'                                     : '9F11',
    'ApplicationPreferredName'                                 : '9F12',
    'LastOnlineApplicationTransactionCounterRegister'          : '9F13',
    'LowerConsecutiveOfflineLimit'                             : '9F14',
    'MerchantCategoryCode'                                     : '9F15',
    'MerchantIdentifier'                                       : '9F16',
    'PersonalIdentificationNumberTryCounter'                   : '9F17',
    'IssuerScriptIdentifier'                                   : '9F18',
    'TerminalCountryCode'                                      : '9F1A',
    'TerminalFloorLimit'                                       : '9F1B',
    'TerminalIdentification'                                   : '9F1C',
    'TerminalRiskManagementData'                               : '9F1D',
    'InterfaceDeviceSerialNumber'                              : '9F1E',
    'Track1DiscretionaryData'                                  : '9F1F',
    'Track2DiscretionaryData'                                  : '9F20',
    'TransactionTime'                                          : '9F21',
    'CertificationAuthorityPublicKeyIndex'                     : '9F22',
    'UpperConsecutiveOfflineLimit'                             : '9F23',
    'ApplicationCryptogram'                                    : '9F26',
    'CryptogramInformationData'                                : '9F27',
    'IntegratedCircuitCardPINEnciphermentPublicKeyCertificate' : '9F2D',
    'IntegratedCircuitCardPINEnciphermentPublicKeyExponent'    : '9F2E',
    'IntegratedCircuitCardPINEnciphermentPublicKeyRemainder'   : '9F2F',
    'IssuerPublicKeyExponent'                                  : '9F32',
    'TerminalCapabilities'                                     : '9F33',
    'CardholderVerificationMethodResults'                      : '9F34',
    'TerminalType'                                             : '9F35',
    'ApplicationTransactionCounter'                            : '9F36',
    'UnpredictableNumber'                                      : '9F37',
    'ProcessingOptionsDataObjectList'                          : '9F38',
    'Point-of-ServiceEntryMode'                                : '9F39',
    'AmountReferenceCurrency'                                  : '9F3A',
    'ApplicationReferenceCurrency'                             : '9F3B',
    'TransactionReferenceCurrencyCode'                         : '9F3C',
    'TransactionReferenceCurrencyExponent'                     : '9F3D',
    'AdditionalTerminalCapabilities'                           : '9F40',
    'TransactionSequenceCounter'                               : '9F41',
    'ApplicationCurrencyCode'                                  : '9F42',
    'ApplicationReferenceCurrencyExponent'                     : '9F43',
    'ApplicationCurrencyExponent'                              : '9F44',
    'DataAuthenticationCode'                                   : '9F45',
    'IntegratedCircuitCardPublicKeyCertificate'                : '9F46',
    'IntegratedCircuitCardPublicKeyExponent'                   : '9F47',
    'IntegratedCircuitCardPublicKeyRemainder'                  : '9F48',
    'DynamicDataAuthenticationDataObjectList'                  : '9F49',
    'StaticDataAuthenticationTagList'                          : '9F4A',
    'SignedDynamicApplicationData'                             : '9F4B',
    'ICCDynamicNumber'                                         : '9F4C',
    'LogEntry'                                                 : '9F4D',
    'MerchantNameandLocation'                                  : '9F4E',
    'LogFormat'                                                : '9F4F',
    'TransactionCategoryCode'                                  : '9F53',
    'FileControlInformationProprietaryTemplate'                : 'A5',
    'FileControlInformationIssuerDiscretionaryData'            : 'BF0C',
}

# Ingenico specific "EMV" tags
doftags.update({
    'TerminalActionCodeDefault'                                : 'DF03',
    'TerminalActionCodeDenial'                                 : 'DF04',
    'TerminalActionCodeOnline'                                 : 'DF05',
    'IssuerScriptResults'                                      : 'DF11',
})
